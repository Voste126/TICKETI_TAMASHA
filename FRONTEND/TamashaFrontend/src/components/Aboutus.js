import React from 'react';
import { MDBContainer, MDBRow, MDBCol } from 'mdb-react-ui-kit';

export default function AboutUs() {
    return (
        <>
            <MDBContainer style={{ marginTop: '50px', maxWidth: '1200px' }}>
                <MDBRow className="align-items-center">
                    {/* Left Column: About Us Text */}
                    <MDBCol md='6'>
                        <div style={{ padding: '30px' }}>
                            <h1 style={{ fontFamily: 'Lobster, cursive', color: '#E63946' }}>
                                About Tiketi Tamasha
                            </h1>
                            <p style={{ fontFamily: 'Poppins, sans-serif', fontSize: '18px', color: '#1D3557', marginTop: '20px', lineHeight: '1.6' }}>
                                Welcome to <span style={{ fontWeight: '600' }}>Tiketi Tamasha</span>, your ultimate platform for event ticketing and management. 
                                We are passionate about making events more accessible and enjoyable for everyone. 
                                From concerts and conferences to festivals and sports events, we ensure that your ticketing experience is smooth, secure, and convenient.
                            </p>
                            <p style={{ fontFamily: 'Poppins, sans-serif', fontSize: '18px', color: '#1D3557', marginTop: '20px', lineHeight: '1.6' }}>
                                At <span style={{ fontWeight: '600' }}>Tiketi Tamasha</span>, we empower event organizers with the tools they need to manage their events efficiently. 
                                Our platform supports variable pricing, calendar integration, and secure payment options, including MPESA. 
                                Join us and discover a new way of experiencing events.
                            </p>
                        </div>
                    </MDBCol>

                    {/* Right Column: Image */}
                    <MDBCol md='6'>
                        <div style={{ textAlign: 'center' }}>
                            <img
                                    src='https://media.istockphoto.com/id/1181169462/photo/are-you-ready-to-party.jpg?s=170667a&w=0&k=20&c=TDHZGHWiB4dg8762I0p1utuR44LjVnYgg8chp_AJsWk='
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
