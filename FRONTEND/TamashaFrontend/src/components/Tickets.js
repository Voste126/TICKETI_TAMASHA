import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import { MDBContainer, MDBRow, MDBCol, MDBCard, MDBCardBody, MDBCardTitle, MDBCardText, MDBCardImage, MDBSpinner, MDBBtn, MDBInput } from 'mdb-react-ui-kit';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

function Tickets() {
    const { event_id } = useParams(); // Get event_id from the URL
    const [tickets, setTickets] = useState([]);
    const [eventDetails, setEventDetails] = useState(null);
    const [loading, setLoading] = useState(true);
    const [quantities, setQuantities] = useState({}); // State to hold ticket quantities

    useEffect(() => {
        const token = localStorage.getItem('access_token'); // Get the token from localStorage

        // Fetch event details
        axios.get(`http://localhost:8000/api/events/${event_id}/`, {
            headers: {
                'Authorization': `Bearer ${token}`,
            },
        })
        .then(response => {
            setEventDetails(response.data); // Set event details
        })
        .catch(error => {
            console.error("Error fetching event details:", error);
        });

        // Fetch tickets for the event
        axios.get(`http://localhost:8000/api/tickets/?event_id=${event_id}`, {
            headers: {
                'Authorization': `Bearer ${token}`,
            },
        })
        .then(response => {
            setTickets(response.data); // Set the tickets data to state
            setLoading(false); // Disable loading once data is fetched
        })
        .catch(error => {
            console.error("Error fetching tickets:", error);
            setLoading(false); // Disable loading even if an error occurs
        });
    }, [event_id]);

    const handleQuantityChange = (ticket_id, value) => {
        setQuantities({
            ...quantities,
            [ticket_id]: value,
        });
    };

    const handleBookTicket = (ticket_id) => {
        const token = localStorage.getItem('access_token'); // Get the token from localStorage
        const quantity = quantities[ticket_id] || 1; // Use entered quantity or default to 1
    
        axios.post('http://localhost:8000/api/bookings/', {
            ticket: ticket_id,  // Send the ticket ID
            event: event_id,    // Send the event ID
            quantity: quantity  // Send the ticket quantity
        }, {
            headers: {
                'Authorization': `Bearer ${token}`,
            },
        })
        .then(response => {
            toast.success('Ticket booked successfully!');
        })
        .catch(error => {
            console.error("Error booking ticket:", error.response.data);
            toast.error('Failed to book ticket. Please try again later.');
        });
    };

    if (loading) {
        return (
            <MDBContainer className="d-flex justify-content-center align-items-center" style={{ minHeight: '100vh' }}>
                <MDBSpinner role="status">
                    <span className="visually-hidden">Loading tickets...</span>
                </MDBSpinner>
            </MDBContainer>
        );
    }

    if (!eventDetails) {
        return <p>Error loading event details. Please try again later.</p>;
    }

    if (tickets.length === 0) {
        return <p>No tickets available for this event.</p>;
    }

    return (
        <MDBContainer className="py-5">
            <ToastContainer />
            {/* Event Details */}
            <MDBCard className="mb-5 shadow-5" style={{ borderRadius: '15px' }}>
                <MDBRow className="g-0">
                    <MDBCol md="6">
                        <MDBCardImage
                            src={eventDetails.image_url || 'https://mdbootstrap.com/img/new/standard/nature/111.webp'} // Default image if not available
                            alt={eventDetails.title}
                            fluid
                            className="rounded-start"
                            style={{ maxHeight: '100%', objectFit: 'cover' }}
                        />
                    </MDBCol>
                    <MDBCol md="6">
                        <MDBCardBody>
                            <MDBCardTitle style={{ fontSize: '2rem', color: '#1D3557' }}>{eventDetails.title}</MDBCardTitle>
                            <MDBCardText style={{ fontSize: '1.2rem', color: '#555', marginBottom: '20px' }}>
                                {eventDetails.description}
                            </MDBCardText>
                            <MDBCardText>
                                <strong>Date:</strong> {new Date(eventDetails.date).toLocaleDateString()}
                            </MDBCardText>
                            <MDBCardText>
                                <strong>Location:</strong> {eventDetails.location}
                            </MDBCardText>
                            <MDBCardText>
                                <strong>Total Tickets Available:</strong> {eventDetails.tickets_available} {/* Display total tickets available */}
                            </MDBCardText>
                        </MDBCardBody>
                    </MDBCol>
                </MDBRow>
            </MDBCard>

            {/* Tickets List */}
            <MDBRow>
                {tickets.map(ticket => (
                    <MDBCol key={ticket.ticket_id} md="4" className="mb-4">
                        <MDBCard className="h-100 shadow-2-strong">
                            <MDBCardBody className="text-center">
                                <MDBCardTitle>{ticket.ticket_type}</MDBCardTitle>
                                <MDBCardText>
                                    <strong>Price:</strong> ${ticket.price}
                                </MDBCardText>
                                <MDBCardText>
                                    <strong>Available Tickets:</strong> {ticket.quantity}
                                </MDBCardText>
                                <MDBInput 
                                    label="Quantity" 
                                    type="number" 
                                    value={quantities[ticket.ticket_id] || 1} 
                                    min="1" 
                                    onChange={(e) => handleQuantityChange(ticket.ticket_id, e.target.value)} 
                                />
                                <MDBBtn
                                    color="success"
                                    className="mt-3"
                                    onClick={() => handleBookTicket(ticket.ticket_id)} // Book ticket on button click
                                >
                                    Book Now
                                </MDBBtn>
                            </MDBCardBody>
                        </MDBCard>
                    </MDBCol>
                ))}
            </MDBRow>
        </MDBContainer>
    );
}

export default Tickets;


