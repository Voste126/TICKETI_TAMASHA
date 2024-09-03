import React from 'react';
import { MDBCarousel, MDBCarouselItem, MDBCarouselCaption, MDBBtn } from 'mdb-react-ui-kit';
export default function Back() {
    return (
        <MDBCarousel showIndicators fade>
            <MDBCarouselItem itemId={1}>
                <img src='https://mdbootstrap.com/img/Photos/Slides/img%20(15).jpg' className='d-block w-100' alt='...' />
                <MDBCarouselCaption>
                    <h5>First slide label</h5>
                    <p>Nulla vitae elit libero, a pharetra augue mollis interdum.</p>
                    <MDBBtn href='/createevent' outline className='mx-2' color='success'>
                            CREATE EVENT
                    </MDBBtn>
                </MDBCarouselCaption>
            </MDBCarouselItem>

            <MDBCarouselItem itemId={2}>
                <img src='https://mdbootstrap.com/img/Photos/Slides/img%20(22).jpg' className='d-block w-100' alt='...' />
                <MDBCarouselCaption>
                    <h5>Second slide label</h5>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
                    <MDBBtn href='/createevent' outline className='mx-2' color='success'>
                            CREATE EVENT
                    </MDBBtn>
                </MDBCarouselCaption>
            </MDBCarouselItem>

            <MDBCarouselItem itemId={3}>
                <img src='https://mdbootstrap.com/img/Photos/Slides/img%20(23).jpg' className='d-block w-100' alt='...' />
                <MDBCarouselCaption>
                    <h5>Third slide label</h5>
                    <p>Praesent commodo cursus magna, vel scelerisque nisl consectetur.</p>
                    <MDBBtn href='/createevent' outline className='mx-2' color='success'>
                            CREATE EVENT
                    </MDBBtn>
                </MDBCarouselCaption>
            </MDBCarouselItem>
        </MDBCarousel>
    );
}