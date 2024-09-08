import React, { useState } from 'react';
import axios from 'axios';
import { useParams, useNavigate } from 'react-router-dom';
import { MDBContainer, MDBCard, MDBCardBody, MDBRow, MDBCol, MDBInput, MDBBtn } from 'mdb-react-ui-kit';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

function CreateEventTicket() {
    const { event_id } = useParams(); // Get event_id from the URL
    const [ticketType, setTicketType] = useState('REGULAR');
    const [price, setPrice] = useState('');
    const [quantity, setQuantity] = useState('');
    const [loading, setLoading] = useState(false);
    const navigate = useNavigate(); // Initialize useNavigate

    const TICKET_CHOICES = [
        { value: 'EARLY_BIRD', label: 'Early Bird' },
        { value: 'REGULAR', label: 'Regular' },
        { value: 'VIP', label: 'VIP' },
        { value: 'VVIP', label: 'VVIP' },
        { value: 'EXECUTIVE', label: 'Executive' },
    ];

    const handleSubmit = (e) => {
        e.preventDefault();
        setLoading(true);
        const token = localStorage.getItem('access_token'); // Get the token from localStorage
        
        axios.post('http://localhost:8000/api/tickets/', {
            event: event_id, // Send the event ID
            ticket_type: ticketType,
            price: parseFloat(price),
            quantity: parseInt(quantity),
        }, {
            headers: {
                'Authorization': `Bearer ${token}`,
            },
        })
        .then(response => {
            toast.success('Ticket created successfully!');
            setLoading(false);
            // set all the fields to empty

            // Redirect to the tickets page
        })
        .catch(error => {
            console.error('Error creating ticket:', error.response.data);
            toast.error('Failed to create ticket. Please try again.');
            setLoading(false);
        });
    };

    return (
        <MDBContainer fluid className="d-flex align-items-center justify-content-center" style={{ minHeight: '100vh', padding: '0' }}>
            <div className="w-100" style={{ backgroundImage: 'url(https://mdbootstrap.com/img/new/textures/full/171.jpg)', backgroundSize: 'cover', backgroundPosition: 'center', padding: '60px 0' }}>
                <MDBCard className='mx-auto my-5 p-5 shadow-5' style={{ maxWidth: '800px', background: 'hsla(0, 0%, 100%, 0.8)', backdropFilter: 'blur(30px)', borderRadius: '15px' }}>
                    <MDBCardBody className='p-5 text-center'>
                        <ToastContainer />
                        <h2 className="fw-bold mb-5">Create Event Ticket</h2>

                        <form onSubmit={handleSubmit}>
                            <MDBRow>
                                <MDBCol md='6'>
                                    <MDBInput 
                                        wrapperClass='mb-4' 
                                        label='Price' 
                                        type='number' 
                                        step='0.01' 
                                        value={price}
                                        onChange={(e) => setPrice(e.target.value)}
                                        required
                                    />
                                </MDBCol>

                                <MDBCol md='6'>
                                    <MDBInput 
                                        wrapperClass='mb-4' 
                                        label='Quantity' 
                                        type='number' 
                                        value={quantity}
                                        onChange={(e) => setQuantity(e.target.value)}
                                        required
                                    />
                                </MDBCol>
                            </MDBRow>

                            <MDBRow>
                                <MDBCol md='12'>
                                    <div className="my-4">
                                        <label htmlFor="ticketType" className="form-label">Ticket Type</label>
                                        <select 
                                            id="ticketType" 
                                            className="form-select" 
                                            value={ticketType} 
                                            onChange={(e) => setTicketType(e.target.value)}
                                            required
                                        >
                                            {TICKET_CHOICES.map(choice => (
                                                <option key={choice.value} value={choice.value}>{choice.label}</option>
                                            ))}
                                        </select>
                                    </div>
                                </MDBCol>
                            </MDBRow>

                            <MDBBtn type='submit' className='w-100 mb-4' size='md' style={{ backgroundColor: '#E63946', color: '#F1FAEE' }} disabled={loading}>
                                {loading ? 'Creating...' : 'Create Ticket'}
                            </MDBBtn>

                            <MDBBtn href={`/events`} className='w-100' size='md' style={{ backgroundColor: '#457B9D', color: '#F1FAEE' }}>
                                Back to Events
                            </MDBBtn>
                        </form>
                    </MDBCardBody>
                </MDBCard>
            </div>
        </MDBContainer>
    );
}

export default CreateEventTicket;

