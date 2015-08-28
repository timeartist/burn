        
        
const messageForm = (<form action="/submit" method="post">
                        <Input name='message' style={{height:'200px'}} type='textarea' label='Private Message:' placeholder='Your Self Destructing Message Goes Here' />
                        <Button style={{float:'right'}} type="submit" bsStyle='primary' right>Submit</Button>
                     </form>);

React.render(messageForm,
             document.getElementById('messageForm')
             );
                     