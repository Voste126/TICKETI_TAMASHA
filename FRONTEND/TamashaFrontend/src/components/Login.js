import React from 'react';
import {
  MDBBtn,
  MDBContainer,
  MDBRow,
  MDBCol,
  MDBInput
} from 'mdb-react-ui-kit';
import './Login.css';

function Login() {
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

            <p style={{ fontSize: '1rem', color: '#343A40' }}>Please login to your account</p>

            <MDBInput wrapperClass='mb-4' label='Email address' id='form1' type='email' style={{ borderColor: '#1D3557' }} />
            <MDBInput wrapperClass='mb-4' label='Password' id='form2' type='password' style={{ borderColor: '#1D3557' }} />

            <div className="text-center pt-1 mb-5 pb-1">
              <MDBBtn href='/' className="mb-4 w-100" style={{ backgroundColor: '#E63946', color: '#F1FAEE' }}>Sign in</MDBBtn>
              <a className="text-muted" href="#!" style={{ textDecoration: 'underline' }}>Forgot password?</a>
            </div>

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
                Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
              </p>
            </div>
          </div>
        </MDBCol>
      </MDBRow>
    </MDBContainer>
  );
}

export default Login;
