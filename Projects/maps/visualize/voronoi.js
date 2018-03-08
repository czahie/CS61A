/* Adapted from https://strongriley.github.io/d3/ex/voronoi.html
 * and http://bl.ocks.org/shimizu/5610671
 */

var clusterColor = d3.scale.category10();
var fillColor = d3.scale.linear().domain([1, 5]).range(["blue", "yellow"]);
var fillOpacity = 0.3;
var hoverOpacity = 0.7;

var tooltip = d3.select("body")
    .append("div")
    .attr("class", "tooltip")
    .style("opacity", 0);

var dotAttributes = {
    "class": "dot",
    "cx": function (d) { return d.x; },
    "cy": function (d) { return d.y; },
    "r": function (d) { return 4; },
    "fill": function (d) { return clusterColor(d.cluster); }
};

var polygonAttributes = {
    "class": "cell",
    "id": function (d) { return makeValidID(d.name).substr(1); },
    "stroke": "black",
    "opacity": fillOpacity,
    "fill": function (d) { return fillColor(d.weight); },
    "d": function (d) { return "M" + d.join("L") + "Z"; }
};

var makeValidID = function (s) {
    return "#" + s.replace(/[^a-zA-Z]/g, "-");
};

var overlay;
VoronoiOverlay.prototype = new google.maps.OverlayView();

function VoronoiOverlay (map, data) {
    // VoronoiOverlay constructor
    this.map_ = map;
    this.data_ = data;
    this.div_ = null;
    this.svg_ = null;
    this.svgOverlay_ = null;

    this.setMap(map);
};

VoronoiOverlay.prototype.onAdd = function () {
    var layer = d3.select(this.getPanes().overlayMouseTarget)
                  .append("div")
                  .attr("id", "svg-overlay-wrapper")
                  .attr("class", "svg-overlay-wrapper");
    var svg = layer.append("svg");
    var svgOverlay = svg.append("g").attr("class", "svg-overlay");

    // enable mouse events on overlay layer
    // stackoverflow.com/q/13912754
    div = layer[0][0];  // get the DOM element <div class="svg-overlay">
    google.maps.event.addDomListener(div, "mouseover", function () {});

    // cache d3 elements
    this.div_ = layer;
    this.svg_ = svg;
    this.svgOverlay_ = svgOverlay;
};

VoronoiOverlay.prototype.draw = function() {
    var self = this;    // store a reference to `this`
    var overlayProjection = this.getProjection();
    var data = this.data_;

    // convert datum d's `x`, `y` (lat, long) into an absolute pixel location
    // on the map, accounting for the svg's offset as defined in voronoi.html
    var googleMapProjection = function (d) {
        var googleCoordinates = new google.maps.LatLng(d.x, d.y);
        var pixelCoordinates = overlayProjection.fromLatLngToDivPixel(googleCoordinates);
        return [pixelCoordinates.x + 4000, pixelCoordinates.y + 4000];
    };

    // update the fields `x`, `y` of each data point using googleMapProjection
    var transformData = function (data) {
        var transformed = [];
        data.forEach(function (val, i, arr) {
            // Create a copy
            var datum = {};
            datum.name = val.name;
            datum.weight = val.weight;
            datum.cluster = val.cluster;

            // Update coordinates with projected coordinates
            var newCoordinates = googleMapProjection(val);
            datum.x = newCoordinates[0];
            datum.y = newCoordinates[1];
            transformed.push(datum);
        });
        return transformed;
    };

    var transformedData = transformData(data);

    var voronoi = d3.geom.voronoi(transformedData.map(function (d) { return [d.x, d.y, d.weight]; }));
    var polygons = voronoi.map(d3.geom.polygon);
    polygons.forEach(function (val, i, arr) {
        val.weight = data[i].weight;
        val.name = data[i].name;
        val.cluster = data[i].cluster;
    });

    this.svgOverlay_.selectAll("path")
        .data(polygons)
        .attr(polygonAttributes)    // "duplicate" attr needed for gmaps zoom to work
        .enter()
        .append("path")
        .attr(polygonAttributes)
        .on("mouseover", function (d, i) {
            self.updateColor(d);
        })
        .on("mousemove", function (d, i) {
            tooltip.transition()
                .duration(100)
                .style("opacity", 0.9);
            tooltip.html(d.name + " (" + Math.round(d.weight * 100) / 100 + ")")
                .style("left", (d3.event.pageX + 5) + "px")
                .style("top", (d3.event.pageY - 28) + "px");
        })
        .on("mouseout", function (d, i) {
            tooltip.transition()
                .duration(200)
                .style("opacity", 0);
            self.resetColor(d);
        });

    this.svgOverlay_.selectAll(".dot")
        .data(transformedData)
        .attr(dotAttributes)
        .enter()
        .append("circle")
        .attr(dotAttributes)
        .on("mouseover", function (d) {
            tooltip.transition()
                .duration(100)
                .style("opacity", 0.9);
            tooltip.html(d.name + " (" + Math.round(d.weight * 100) / 100 + ")")
                .style("left", (d3.event.pageX + 5) + "px")
                .style("top", (d3.event.pageY - 28) + "px");
            self.updateColor(d);
        })
        .on("mouseout", function (d) {
            tooltip.transition()
                .duration(200)
                .style("opacity", 0);
            self.resetColor(d);
        });
};

VoronoiOverlay.prototype.updateColor = function (d, i) {
    this.svg_.select(makeValidID(d.name))
        .style("opacity", hoverOpacity)
        .style("fill", function (d) { return clusterColor(d.cluster); });
};

VoronoiOverlay.prototype.resetColor = function (d, i) {
    this.svgOverlay_.select(makeValidID(d.name))
        .style("opacity", fillOpacity)
        .style("fill", function (d) { return fillColor(d.weight); });
};



d3.json("voronoi.json", function (data) {

    var map = new google.maps.Map(document.getElementById("map-canvas"), {
        zoom: 16,
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        center: new google.maps.LatLng(37.872, -122.26),
    });

    overlay = new VoronoiOverlay(map, data);

});
