import React, {useState} from 'react';
import axios from 'axios';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

import {
  MDBBtn,
  MDBContainer,
  MDBRow,
  MDBCol,
  MDBInput
} from 'mdb-react-ui-kit';
import './Login.css';

function Login() {
    const [credentials, setCredentials] = useState({ email: '', password: '' });
    const apiUrl = process.env.REACT_APP_API_URL;
    const handleChange = (e) => {
    setCredentials({ ...credentials, [e.target.name]: e.target.value });
  };

  const handleLogin = (e) => {
    e.preventDefault();
    axios.post(`${apiUrl}auth/login/`, credentials)
      .then(response => {
        localStorage.setItem('access_token', response.data.token.access);
        localStorage.setItem('refresh_token', response.data.token.refresh);
        toast.success("Login successful!");
        setTimeout(() => {
          window.location.href = '/';
        }, 5000);
      })
      .catch(error => {
        toast.error("Login failed. Please try again.");
      });
  };

  return (
    <MDBContainer className="my-5 gradient-form" style={{ maxWidth: '900px', borderRadius: '10px', boxShadow: '0px 4px 15px rgba(0, 0, 0, 0.1)' }}>
      <MDBRow className="g-0">
        {/* Left Side - Login Form */}
        <MDBCol col='6'>
          <div className="d-flex flex-column p-4">
            <div className="text-center">
              <img
                src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-login-form/lotus.webp"
                style={{ width: '150px' }}
                alt="logo"
              />
              <h4 className="mt-3 mb-4 pb-1" style={{ fontWeight: 'bold', color: '#1D3557' }}>Ticketi Tamasha</h4>
            </div>
            <ToastContainer />
            <p style={{ fontSize: '1rem', color: '#343A40' }}>Please login to your account</p>

            <form onSubmit={handleLogin}>
            <MDBInput  label='Email' name='email' onChange={handleChange} type='email' style={{ borderColor: '#1D3557' }} className='mb-4' required />
            <MDBInput  label='Password' name='password' onChange={handleChange} type='password'style={{ borderColor: '#1D3557' }} className='mb-4' required />
            <div className="text-center pt-1 mb-5 pb-1"><a className="text-muted" href="#!" style={{ textDecoration: 'underline' }}>Forgot password?</a>
            <MDBBtn  className="mb-4 w-100" type='submit' style={{ backgroundColor: '#E63946', color: '#F1FAEE' }}>Login</MDBBtn>
            </div>
          </form>
            <div className="d-flex flex-row align-items-center justify-content-center pb-4">
              <p className="mb-0">Don't have an account?</p>
              <MDBBtn href='/signup' outline className='mx-2' color='danger' style={{ borderColor: '#E63946', color: '#E63946' }}>
                Sign Up
              </MDBBtn>
            </div>
          </div>
        </MDBCol>

        {/* Right Side - Information Section */}
        <MDBCol col='6'>
          <div className="d-flex flex-column justify-content-center gradient-custom-2 h-100" style={{ background: 'linear-gradient(45deg, #457B9D, #1D3557)', borderRadius: '0 10px 10px 0' }}>
            <div className="text-white px-4 py-5">
              <h4 className="mb-4" style={{ fontWeight: 'bold' }}>We are more than just a company</h4>
              <p className="small mb-0">
                We are more than just a Friend. We are a Family. We are here to help you with all your event needs.
              </p>
            </div>
          </div>
        </MDBCol>
      </MDBRow>
    </MDBContainer>
  );
}

export default Login;
