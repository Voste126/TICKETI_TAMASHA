import React, { useState } from 'react';
import {
  MDBBtn,
  MDBContainer,
  MDBRow,
  MDBCol,
  MDBInput,
  MDBSelect,
  MDBSelectInput,
  MDBSelectOptions,
  MDBSelectOption
} from 'mdb-react-ui-kit';


function PaymentForm() {
  const [paymentMethod, setPaymentMethod] = useState('');

  const handlePaymentMethodChange = (e) => {
    setPaymentMethod(e.target.value);
  };

  return (
    <MDBContainer className="my-5 gradient-form" style={{ maxWidth: '900px', borderRadius: '10px', boxShadow: '0px 4px 15px rgba(0, 0, 0, 0.1)' }}>
      <MDBRow className="g-0">
        {/* Payment Form */}
        <MDBCol col='12'>
          <div className="d-flex flex-column p-4">
            <div className="text-center">
              <img
                src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-login-form/lotus.webp"
                style={{ width: '150px' }}
                alt="logo"
              />
              <h4 className="mt-3 mb-4 pb-1" style={{ fontWeight: 'bold', color: '#1D3557' }}>Tiketi Tamasha</h4>
            </div>

            <p style={{ fontSize: '1rem', color: '#343A40' }}>Please complete your payment</p>

            <MDBInput wrapperClass='mb-4' label='Booking ID' id='form1' type='text' style={{ borderColor: '#1D3557' }} />
            <MDBInput wrapperClass='mb-4' label='Amount' id='form2' type='number' style={{ borderColor: '#1D3557' }} />

            <select
              className="mb-4 form-select"
              value={paymentMethod}
              onChange={handlePaymentMethodChange}
              style={{ borderColor: '#1D3557' }}
            >
              <option value="">Select Payment Method</option>
              <option value="MP">MPESA</option>
              <option value="CC">Credit Card</option>
              <option value="DC">Debit Card</option>
              <option value="MC">MasterCard</option>
            </select>

            {paymentMethod === 'MP' && (
              <MDBInput wrapperClass='mb-4' label='Phone Number' id='form3' type='tel' style={{ borderColor: '#1D3557' }} />
            )}

            {paymentMethod === 'CC' || paymentMethod === 'DC' || paymentMethod === 'MC' ? (
              <>
                <MDBInput wrapperClass='mb-4' label='Card Number' id='form4' type='text' style={{ borderColor: '#1D3557' }} />
                <MDBInput wrapperClass='mb-4' label='Card Expiry Date' id='form5' type='text' style={{ borderColor: '#1D3557' }} />
                <MDBInput wrapperClass='mb-4' label='CVV' id='form6' type='text' style={{ borderColor: '#1D3557' }} />
              </>
            ) : null}

            <div className="text-center pt-1 mb-5 pb-1">
              <MDBBtn className="mb-4 w-100" style={{ backgroundColor: '#E63946', color: '#F1FAEE' }}>Make Payment</MDBBtn>
            <MDBBtn href='/' className='w-100 mb-4' size='md' style={{ backgroundColor: 'green', color: '#F1FAEE' }}>Back To home</MDBBtn>
            </div>
          </div>
        </MDBCol>
      </MDBRow>
    </MDBContainer>
  );
}

export default PaymentForm;


