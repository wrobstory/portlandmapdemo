Portland Map Demo
================
![final](http://farm4.staticflickr.com/3806/9130557737_ae93c4f471.jpg)

This repo contains the data referenced in the blog post [Creating and Publishing Maps with D3, Dymo, and PhantomJS](http://wrobstory.github.io/2013/06/creating-with-d3-dymo.html). 

The data description and sources are as follows: 

* Shapefiles: [Portland Data Catalog](http://www.portlandoregon.gov/bts/article/268487)
* dymo_input.csv: Input for [Dymo](https://github.com/migurski/Dymo)
* dymo_prep.py: Python Dymo prep tool
* index.html: D3.js code for map
* labels_overlap.json, .topo.json: Dymo labels including overlapping labels
* labels.json, .topo.json: Dymo labels not including overlaps
* mymap.pdf: Example of map rendered to PDF with PhantomJS
* neighborhoods.geojson, .topo.json: Portland Shapefile data converted to geojson with GDAL, then to TopoJSON
* points.json: Dymo point ouput, centered on neighborhood centroids
* rasterize.js: Script from PhantomJS [examples](https://github.com/ariya/phantomjs/blob/master/examples/rasterize.js) folder, BSD licensed

Everything but the rasterize.js script and original Shapefile data is MIT licensed. 
