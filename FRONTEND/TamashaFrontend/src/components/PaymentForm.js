import React, { useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import axios from 'axios';
import {
  MDBContainer,
  MDBRow,
  MDBCol,
  MDBCard,
  MDBCardBody,
  MDBCardTitle,
  MDBBtn,
  MDBInput,
} from 'mdb-react-ui-kit';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

function PaymentForm() {
  const { booking_id } = useParams(); // Use the booking ID from the URL
  const [paymentMethod, setPaymentMethod] = useState('MP');
  const [phoneNumber, setPhoneNumber] = useState('');
  const [amount, setAmount] = useState('');
  const navigate = useNavigate();

  const handlePaymentMethodChange = (e) => {
    setPaymentMethod(e.target.value);
  };

  const handlePhoneNumberChange = (e) => {
    setPhoneNumber(e.target.value);
  };

  const handlePayment = async () => {
    const apiUrl = process.env.REACT_APP_API_URL;
    const token = localStorage.getItem('access_token'); // Get the token from localStorage
    const paymentData = {
      booking_id: booking_id, // Pass the booking_id to the backend
      amount: amount,
      payment_method: paymentMethod,
      ...(paymentMethod === 'MP' && { phone_number: phoneNumber }), // Add phone_number if MPESA is selected
    };

    try {
      const response = await axios.post('https://ticketi-tamasha-1.onrender.com/api/payments/', paymentData, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      toast.success('Payment successful!');
      setInterval(() => {
        navigate('/events'); // Redirect to success page after payment
      }
      , 4000);
 // Redirect to success page after payment
    } catch (error) {
      toast.error('Payment failed. Please try again.');
    }
  };

  return (
    <MDBContainer className="py-5">
      <MDBRow className="justify-content-center">
        <MDBCol md="6">
          <MDBCard className="shadow-5" style={{ borderRadius: '15px' }}>
            <MDBCardBody>
              <MDBCardTitle className="text-center mb-4">Payment Form</MDBCardTitle>
              <ToastContainer />
              {/* Amount Input */}
              <MDBInput
                label="Amount"
                type="number"
                value={amount}
                onChange={(e) => setAmount(e.target.value)}
                required
                className="mb-4"
              />

              {/* Payment Method Select */}
              <div className="mb-4">
                <label htmlFor="paymentMethod" className="form-label">
                  Payment Method
                </label>
                <select
                  id="paymentMethod"
                  className="form-select"
                  value={paymentMethod}
                  onChange={handlePaymentMethodChange}
                >
                  <option value="MP">MPESA</option>
                  <option value="CC">Credit Card</option>
                  <option value="DC">Debit Card</option>
                  <option value="MC">MasterCard</option>
                </select>
              </div>

              {/* Phone Number Input for MPESA */}
              {paymentMethod === 'MP' && (
                <MDBInput
                  label="Phone Number"
                  type="tel"
                  value={phoneNumber}
                  onChange={handlePhoneNumberChange}
                  required
                  className="mb-4"
                />
              )}

              <MDBBtn color="success" className="mt-3" onClick={handlePayment}>
                Pay Now
              </MDBBtn>
            </MDBCardBody>
          </MDBCard>
        </MDBCol>
      </MDBRow>
    </MDBContainer>
  );
}

export default PaymentForm;

