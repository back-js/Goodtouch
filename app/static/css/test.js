import React, {Component} from 'react';
import styled from 'styled-components';
import button_img from "./button_img.png"

class HandleFile extends Component{
    constructor(props) {
        super(props);
        this.webcamRef = React.createRef();
        this.state = {
          file : '',
          previewURL : ''
        }
      }

    handleFileOnChange = (event) => {
    event.preventDefault();
    let reader = new FileReader();
    let file = event.target.files[0];
    reader.onloadend = () => {
        this.setState({
        file : file,
        previewURL : reader.result
        })
    }
    reader.readAsDataURL(file);
    }

    render(){
        const Button = styled.button`
        /* Insert your favorite CSS code to style a button */
            box-sizing: border-box;
            border-radius: 6px;
            background-color: #FFF;
            border: 2px solid #828282;
            position : absolute;
            top: 10%; 
            left: 20%;

            width:100%;
            height: 100%;
            padding:0;
        `;

        const hiddenFileInput = this.webcamRef

        const handleClick = (event) => {
          hiddenFileInput.current.click();
        };

        let profile_preview = null;
        if(this.state.file !== ''){
          profile_preview = <img className='profile_preview' src={this.state.previewURL}></img>
        }
        return(
            <div>
            {profile_preview}
            <Button onClick={handleClick}>
            <img src = "{% static "img/button_img.png" %}"></img>
            <input type='file'
                ref={hiddenFileInput}
                accept='image/jpg,impge/png,image/jpeg,image/gif'
                name='source_image'
                onChange={this.handleFileOnChange}
                style={{display:'none'}}
               >
            </input>
            </Button>
            </div>

        );
    }

}
export default HandleFile;