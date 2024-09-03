import React from 'react';
import { MDBRow, MDBCol } from 'mdb-react-ui-kit';
import EventCard from './EventCard';
import Navbar from './Navbar';

export default function EventList() {
  return (
    <>
    <Navbar />
    <MDBRow className='g-4'>
      <MDBCol md='4'>
        <EventCard />
      </MDBCol>
      <MDBCol md='4'>
        <EventCard />
      </MDBCol>
      <MDBCol md='4'>
        <EventCard />
      </MDBCol>
    </MDBRow>
    </>
  );
}
