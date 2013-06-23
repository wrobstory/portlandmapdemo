var d3 = require('d3')
var topojson = require('topojson')
var data;
d3.json('neighborhoods.topo.json', function(error, neighborhoods) {
    data = neighborhoods;
});