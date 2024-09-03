import React from 'react';
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
  return (
    <MDBContainer fluid className="d-flex align-items-center justify-content-center" style={{ minHeight: '100vh', padding: '0' }}>
      <div className="w-100" style={{ backgroundImage: 'url(https://mdbootstrap.com/img/new/textures/full/171.jpg)', backgroundSize: 'cover', backgroundPosition: 'center', padding: '60px 0' }}>
        
        <MDBCard className='mx-auto my-5 p-5 shadow-5' style={{ maxWidth: '600px', background: 'hsla(0, 0%, 100%, 0.8)', backdropFilter: 'blur(30px)', borderRadius: '15px' }}>
          <MDBCardBody className='p-5 text-center'>

            <h2 className="fw-bold mb-5">Sign up now</h2>

            <MDBRow>
              <MDBCol md='6'>
                <MDBInput wrapperClass='mb-4' label='First name' id='form1' type='text' />
              </MDBCol>

              <MDBCol md='6'>
                <MDBInput wrapperClass='mb-4' label='Last name' id='form2' type='text' />
              </MDBCol>
            </MDBRow>

            <MDBInput wrapperClass='mb-4' label='Email' id='form3' type='email' />
            <MDBInput wrapperClass='mb-4' label='Password' id='form4' type='password' />

            <div className='d-flex justify-content-center mb-4'>
              <MDBCheckbox name='flexCheck' value='' id='flexCheckDefault' label='Subscribe to our newsletter' />
            </div>

            <MDBBtn href='/login' className='w-100 mb-4' size='md' style={{ backgroundColor: '#E63946', color: '#F1FAEE' }}>Sign up</MDBBtn>

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
