var Navbar = ReactBootstrap.Navbar;
var Nav = ReactBootstrap.Nav;
var NavItem = ReactBootstrap.NavItem;
var Input = ReactBootstrap.Input;
var Button = ReactBootstrap.Button

const nav = (React.createElement(Navbar, {left: true, brand: React.createElement("img", {src: "/static/img/fan_h_web.png"}), inverse: true})
     );

React.render(nav,
             document.getElementById('nav')
             );
