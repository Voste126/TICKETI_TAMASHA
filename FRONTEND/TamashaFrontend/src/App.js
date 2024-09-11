import React from 'react';
import Login from './components/Login';
import SignUp from './components/Signup';
import Layout from './components/Layout';
import EventCard from './components/EventCard';
import EventList from './components/EventList';
import CreateEvent from './components/CreateEvent';
import PaymentForm from './components/PaymentForm';
import EventDetails from './components/EventDetails';
import CreateEventTicket from './components/createTickets';
import Tickets from './components/Tickets';



import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
function App() {
  return (
    <Router>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<SignUp />} />
        <Route path="/" element={<Layout />} />
        <Route path="/eventcard" element={<EventCard />} />
        <Route path="/events" element={<EventList />} />
        <Route path="/createevent" element={<CreateEvent />} />
        <Route path="/event/:event_id/ticket" element={<CreateEventTicket />} />
        <Route path="/payment/:booking_id" element={<PaymentForm />} />
        <Route path="/events/:event_id" element={<EventDetails/>} />
        <Route path="/event/:event_id/tickets/" element={<Tickets />} />
      </Routes>
    </Router>
  );
};
export default App;
