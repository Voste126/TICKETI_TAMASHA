import React from 'react';
import { MDBContainer, MDBRow, MDBCol, MDBInput, MDBBtn, MDBIcon } from 'mdb-react-ui-kit';


export default function Contactus() {
    return (
        <>
            <MDBContainer style={{ marginTop: '50px', maxWidth: '1200px' }}>
                <MDBRow className="align-items-center">
                    {/* Left Column: Contact Form */}
                    <MDBCol md='6'>
                        <form style={{ padding: '30px', borderRadius: '10px', backgroundColor: '#ffffff', boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)' }}>
                            <p className='h4 text-center mb-4' style={{ color: '#E63946' }}>Contact Us</p>
                            <div className='grey-text'>
                                <MDBInput label='Your name' icon='user' group type='text' validate error='wrong' success='right' className='mb-4' />
                                <MDBInput label='Your email' icon='envelope' group type='email' validate error='wrong' success='right' className='mb-4' />
                                <MDBInput label='Subject' icon='tag' group type='text' validate error='wrong' success='right' className='mb-4' />
                                <MDBInput type='textarea' rows='4' label='Your message' icon='pencil-alt' className='mb-4' />
                            </div>
                            <div className='text-center'>
                                <MDBBtn style={{ backgroundColor: '#1D3557', color: '#F1FAEE', borderColor: '#E63946' }}>
                                    <MDBIcon far icon='paper-plane' className='mr-2' /> Send
                                </MDBBtn>
                            </div>
                        </form>
                    </MDBCol>

                    {/* Right Column: Image */}
                    <MDBCol md='6'>
                        <div style={{ textAlign: 'center' }}>
                            <img
                                    src='https://mdbootstrap.com/img/new/standard/city/042.webp'
                                    className='img-fluid shadow-2-strong'
                                    alt='Contact Us' style={{ width: '100%', borderRadius: '10px', boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)' }}
                                    />
                        </div>
                    </MDBCol>
                </MDBRow>
            </MDBContainer>
        </>
    );
}
