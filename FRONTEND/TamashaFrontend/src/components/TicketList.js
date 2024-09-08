import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';
import { MDBCard, MDBCardBody, MDBCardTitle, MDBBtn, MDBInput } from 'mdb-react-ui-kit';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

export default function TicketList() {
  const [tickets, setTickets] = useState([]);
  const { eventId } = useParams();
  const [quantity, setQuantity] = useState(1);

    useEffect(() => {
  const fetchTickets = async () => {
    try {
      const token = localStorage.getItem('access_token');
      if (!token) {
        toast.error('No authentication token found. Please log in.');
        return;
      }

      const response = await axios.get(`http://localhost:8000/api/tickets/?event_id=${eventId}`, {
        headers: {
          'Authorization': `Bearer ${token}`,
        },
      });

      setTickets(response.data);
    } catch (error) {
      if (error.response && error.response.status === 403) {
        toast.error('You are not authorized to access tickets. Please log in.');
      } else {
        toast.error('Failed to fetch tickets.');
      }
    }
  };

  if (eventId) {
    fetchTickets();  // Only fetch if eventId is valid
  }
}, [eventId]);


  const handleBookTicket = async (ticketId, availableQuantity) => {
    const token = localStorage.getItem('access_token');

    if (quantity > availableQuantity) {
      toast.error('Not enough tickets available.');
      return;
    }

    const bookingData = {
      ticket_id: ticketId,
      event_id: eventId,
      quantity: quantity,
    };

    try {
      await axios.post('http://localhost:8000/api/bookings/', bookingData, {
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json',
        },
      });

      // Update the ticket quantity in real-time
      setTickets((prevTickets) =>
        prevTickets.map((ticket) =>
          ticket.ticket_id === ticketId
            ? { ...ticket, quantity: ticket.quantity - quantity }
            : ticket
        )
      );

      toast.success('Ticket booked successfully!');
    } catch (error) {
      toast.error('Booking failed. Please try again.');
    }
  };

  return (
    <>
      <ToastContainer />
      <div>
        {tickets.map((ticket) => (
          <MDBCard key={ticket.ticket_id}>
            <MDBCardBody>
              <MDBCardTitle>{ticket.ticket_type} - ${ticket.price}</MDBCardTitle>
              <p>
                {ticket.quantity > 0
                  ? `Quantity available: ${ticket.quantity}`
                  : 'Out of order'}
              </p>
              
              {ticket.quantity > 0 && (
                <>
                  <MDBInput
                    type="number"
                    min="1"
                    max={ticket.quantity}
                    value={quantity}
                    onChange={(e) => setQuantity(e.target.value)}
                    label='Quantity'
                  />
                  <MDBBtn
                    onClick={() => handleBookTicket(ticket.ticket_id, ticket.quantity)}
                  >
                    Book Ticket
                  </MDBBtn>
                </>
              )}

              {ticket.quantity === 0 && <MDBBtn disabled>Out of Order</MDBBtn>}
            </MDBCardBody>
          </MDBCard>
        ))}
      </div>
    </>
  );
}

