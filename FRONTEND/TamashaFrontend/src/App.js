import React from 'react';
import { MDBContainer } from 'mdb-react-ui-kit';
import Login from './components/Login';
import SignUp from './components/Signup';
import Layout from './components/Layout';
import EventCard from './components/EventCard';
import EventList from './components/EventList';
import CreateEvent from './components/CreateEvent';
import PaymentForm from './components/PaymentForm';

import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
function App() {
  return (
    <Router>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<SignUp />} />
        <Route path="/" element={<Layout />} />
        <Route path="/eventcard" element={<EventCard />} />
        <Route path="/eventlist" element={<EventList />} />
        <Route path="/createevent" element={<CreateEvent />} />
        <Route path="/pay" element={<PaymentForm />} />
      </Routes>
    </Router>
  );
};
export default App;
