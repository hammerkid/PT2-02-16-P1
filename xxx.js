/**
 * Created by igor on 17.5.17.
 */
var fs, fsExtra, bluebird, cheerio, request, iconvLite, requestDebug, YRANGE, CRANGE, root, fetchParams, fetchVars, fetchData, iterateList;
fs = require('fs');
fsExtra = require('fs-extra');
bluebird = require('bluebird');
cheerio = require('cheerio');
request = require('request');
iconvLite = require('iconv-lite');
requestDebug = require('request-debug');
YRANGE = 17;
CRANGE = 24;
root = 'http://statdb.dgbas.gov.tw/pxweb';
fetchParams = function(){
  return new bluebird(function(res, rej){
    return request({
      url: root + "/dialog/CityItemlist_n.asp",
      encoding: null,
      method: 'GET'
    }, function(e, r, b){
      var ret;
      if (e) {
        return rej(e + " ( fetch-params )");
      }
      b = iconvLite.decode(new Buffer(b), 'big5').split('<td');
      ret = b.map(function(it){
        return /<input[^>]+value="([^"]+)"[^>]*>/g.exec(it);
      }).filter(function(it){
        return it;
      }).map(function(it){
        return it[1];
      }).filter(function(it){
        return /\d+/.exec(it);
      });
      ret.sort(function(a, b){
        if (b > a) {
          return 1;
        }
        if (a > b) {
          return -1;
        }
        return 0;
      });
      return res(ret);
    });
  });
};
fetchVars = function(params){
  return new bluebird(function(res, rej){
    return request({
      url: root + "/dialog/CityDbQuery2Px_n.asp",
      method: 'POST',
      qsStringifyOptions: {
        arrayFormat: 'repeat'
      },
      encoding: null,
      form: {
        chkSelTableItem: params || []
      }
    }, function(e, r, b){
      var ret, url, matrix;
      if (e) {
        return rej(e + " ( fetch-vars )");
      }
      ret = iconvLite.decode(new Buffer(b), 'big5');
      url = /url=([^']+)/.exec(ret);
      if (!url) {
        return rej("url not parsed ( fetch-vars ) ");
      }
      matrix = /ma=([^&]+)&/.exec(url[1]);
      if (!matrix) {
        return rej("matrxi not parsed ( fetch-vars )");
      }
      return res(matrix[1]);
    });
  });
};
fetchData = function(matrix, length){
  return new bluebird(function(res, rej){
    var i;
    return request({
      url: root + "/Dialog/Saveshow.asp",
      method: 'POST',
      qsStringifyOptions: {
        arrayFormat: 'repeat'
      },
      encoding: null,
      form: {
        Valdavarden1: length,
        Valdavarden2: YRANGE,
        Valdavarden3: CRANGE,
        values1: (function(){
          var i$, to$, results$ = [];
          for (i$ = 1, to$ = length; i$ <= to$; ++i$) {
            i = i$;
            results$.push(i);
          }
          return results$;
        }()),
        values2: (function(){
          var i$, to$, results$ = [];
          for (i$ = 1, to$ = YRANGE; i$ <= to$; ++i$) {
            i = i$;
            results$.push(i);
          }
          return results$;
        }()),
        values3: (function(){
          var i$, to$, results$ = [];
          for (i$ = 1, to$ = CRANGE; i$ <= to$; ++i$) {
            i = i$;
            results$.push(i);
          }
          return results$;
        }()),
        matrix: matrix,
        root: "../database/CountyStatistics/",
        classdir: "../database/CountyStatistics/",
        noofvar: 3,
        elim: "NNN",
        numberstub: 2,
        lang: 9,
        hasAggregno: 0,
        stubceller: YRANGE * length,
        headceller: CRANGE,
        pxkonv: "px"
      }
    }, function(e, r, b){
      var ret;
      if (e) {
        return rej(e + " ( fetch-data ) ");
      }
      ret = iconvLite.decode(new Buffer(b), 'big5');
      return res(ret);
    });
  });
};
iterateList = function(list, prev, count){
  var prefix, re, target, release;
  prev == null && (prev = null);
  count == null && (count = 1);
  if (!list || !list.length) {
    console.log("finished.");
    return;
  }
  prefix = list[0].substring(0, 2);
  if (prefix !== prev) {
    count = 1;
  }
  re = new RegExp("^" + prefix);
  target = list.filter(function(it){
    return re.exec(it);
  });
  list = list.filter(function(it){
    return !re.exec(it);
  });
  if (target.length > 50) {
    release = target.splice(0, 50);
    list = release.concat(list);
  }
  console.log("remaining " + list.length + " index, deal with " + prefix + " type ( " + target.length + " in total )");
  return fetchVars(target).then(function(matrix){
    return fetchData(matrix, target.length);
  }).then(function(res){
    fsExtra.mkdirs('raw/county');
    fs.writeFileSync("raw/county/" + prefix + ('-' + count) + ".px", res);
    return iterateList(list, prefix, count + 1);
  })['catch'](function(it){
    return console.log("failed due to ", it);
  });
};
fetchParams().then(function(list){
  return iterateList(list);
})['catch'](function(it){
  return console.log("failed due to ", it);
});
