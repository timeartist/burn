var Navbar = ReactBootstrap.Navbar;
var Nav = ReactBootstrap.Nav;
var NavItem = ReactBootstrap.NavItem;
var Input = ReactBootstrap.Input;
var Button = ReactBootstrap.Button

const nav = (<Navbar left brand={<img src='/static/img/fan_h_web.png'/>} inverse/>
     );

React.render(nav,
             document.getElementById('nav')
             );
