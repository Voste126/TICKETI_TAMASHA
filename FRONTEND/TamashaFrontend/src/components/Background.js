import React from 'react';
import { MDBCarousel, MDBCarouselItem, MDBCarouselCaption, MDBBtn } from 'mdb-react-ui-kit';
export default function Back() {
    return (
        <MDBCarousel showIndicators fade>
    <MDBCarouselItem itemId={1}>
        <img 
            src='https://cdn.shopify.com/s/files/1/0869/7984/files/slideshow01.jpg?35' 
            className='d-block w-100' 
            alt='' 
            style={{ maxHeight: '800px', objectFit: '' }} 
        />
        <MDBCarouselCaption>
            <h5>upcoming Solo concert</h5>
            <p>Book with us a space and reach a huge audience.</p>
            <MDBBtn href='/createevent' className='me-1' color='success'>
                CREATE EVENT
            </MDBBtn>
        </MDBCarouselCaption>
    </MDBCarouselItem>

            <MDBCarouselItem itemId={2}>
                <img src='https://www.sftravel.com/sites/default/files/styles/hero/public/2024-04/PORTOLA22_Quinn%20Tucker_113556%40QUASARMEDIA.jpg.webp?itok=OXGhkYPK' className='d-block w-100' alt='...' 
                style={{ maxHeight: '800px', objectFit: '' }} />
                <MDBCarouselCaption>
                    <h5>Having a concert?</h5>
                    <p>post it in Ticketi Tamasha and have a vibrant crowd.</p>
                    <MDBBtn href='/createevent'  className='me-1' color='warning'>
                            CREATE EVENT
                    </MDBBtn>
                </MDBCarouselCaption>
            </MDBCarouselItem>

            <MDBCarouselItem itemId={3}>
                <img src='https://thumbs.dreamstime.com/b/young-people-having-fun-rock-concert-live-concert-bright-stage-lights-smoke-dj-performing-ai-generated-people-having-331814355.jpg' 
                className='d-block w-100' 
                alt='...' 
                style={{ maxHeight: '800px', objectFit: '' }} 
                />
                <MDBCarouselCaption>
                    <h5>Are you a DJ or band Player</h5>
                    <p>Book a session and post your event and get hper music lovers.</p>
                    <MDBBtn href='/createevent'  className='me-1' color='danger'>
                            CREATE EVENT
                    </MDBBtn>
                </MDBCarouselCaption>
            </MDBCarouselItem>
        </MDBCarousel>
    );
}