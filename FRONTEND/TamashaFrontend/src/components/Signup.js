import React, {useState} from 'react';
import axios from 'axios';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

import {
  MDBBtn,
  MDBContainer,
  MDBCard,
  MDBCardBody,
  MDBCol,
  MDBRow,
  MDBInput,
  MDBCheckbox,
  MDBIcon
} from 'mdb-react-ui-kit';

function SignUp() {
  const apiUrl = process.env.REACT_APP_API_URL;
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password: ''
  });

  const handleInputChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post('https://ticketi-tamasha-1.onrender.com/auth/signup/', formData)
      .then(response => {
        toast.success("Signup Successful!");
        // move to the login form after successful signup in about 5 seconds
        setTimeout(() => {
          window.location.href = '/login';
        }, 5000);
      })
      .catch(error => {
        toast.error("Signup Failed. Please try again.");
      });
  };



  return (
    <MDBContainer fluid className="d-flex align-items-center justify-content-center" style={{ minHeight: '100vh', padding: '0' }}>
      <div className="w-100" style={{ backgroundImage: 'url(https://mdbootstrap.com/img/new/textures/full/171.jpg)', backgroundSize: 'cover', backgroundPosition: 'center', padding: '60px 0' }}>
        
        <MDBCard className='mx-auto my-5 p-5 shadow-5' style={{ maxWidth: '600px', background: 'hsla(0, 0%, 100%, 0.8)', backdropFilter: 'blur(30px)', borderRadius: '15px' }}>
          <MDBCardBody className='p-5 text-center'>
          <ToastContainer />
            <h2 className="fw-bold mb-5">Sign up now</h2>
          <form onSubmit={handleSubmit}>
            <MDBInput  label='Username' name='username' onChange={handleInputChange} className='mb-4' required />
            <MDBInput  label='Email' name='email' type='email' onChange={handleInputChange} className='mb-4' required />
            <MDBInput  label='Password' name='password' type='password' onChange={handleInputChange} className='mb-4' required />
            <MDBBtn  type='submit' size='md' className='w-100 mb-4' style={{ backgroundColor: '#E63946', color: '#F1FAEE' }}>Sign up</MDBBtn>
            <div className='d-flex justify-content-center mb-4'>
              <MDBCheckbox name='flexCheck' value='' id='flexCheckDefault' label='Subscribe to our newsletter' />
            </div>
          </form>
            <div className="text-center">

              <p>or sign up with:</p>

              <MDBBtn tag='a' color='none' className='mx-3' style={{ color: '#3b5998' }}>
                <MDBIcon fab icon='facebook-f' size="sm" />
              </MDBBtn>

              <MDBBtn tag='a' color='none' className='mx-3' style={{ color: '#1DA1F2' }}>
                <MDBIcon fab icon='twitter' size="sm" />
              </MDBBtn>

              <MDBBtn tag='a' color='none' className='mx-3' style={{ color: '#DB4437' }}>
                <MDBIcon fab icon='google' size="sm" />
              </MDBBtn>

              <MDBBtn tag='a' color='none' className='mx-3' style={{ color: '#333' }}>
                <MDBIcon fab icon='github' size="sm" />
              </MDBBtn>

            </div>

          </MDBCardBody>
        </MDBCard>

      </div>
    </MDBContainer>
  );
}

export default SignUp;
