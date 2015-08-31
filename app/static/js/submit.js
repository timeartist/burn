        
        
const messageForm = (React.createElement("form", {action: "/", method: "post"}, 
                        React.createElement(Input, {name: "message", style: {height:'200px'}, type: "textarea", label: "Private Message:", placeholder: "Your Self Destructing Message Goes Here"}), 
                        React.createElement(Button, {style: {float:'right'}, type: "submit", bsStyle: "primary", right: true}, "Submit")
                     ));

React.render(messageForm,
             document.getElementById('messageForm')
             );
                     