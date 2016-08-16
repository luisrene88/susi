
var ProductoFull = React.createClass({
  displayName: "ProductoFull",

  render: function () {
    return React.createElement(
      "div",
      { className: "tablet-80 tablet-main-center" },
      React.createElement("div", { className: "tablet-10" }),
      React.createElement("div", { className: "tablet-50" }),
      React.createElement("div", { className: "tablet-40" })
    );
  }

});