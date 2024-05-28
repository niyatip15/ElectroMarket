import Header from './components/Header';
import Footer from './components/Footer';
import HomeScreen from './screens/HomeScreen';
import { Container } from 'react-bootstrap';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'; // Import Routes

function App() {
  return (
    <Router>
      <Header />
      <main className='py-3'>
        <Container>
          {/* Use Routes component to wrap Route components */}
          <Routes>
            <Route path='/' element={<HomeScreen />} exact />
          </Routes>
        </Container>
      </main>
      <Footer />
    </Router>
  );
}

export default App;
