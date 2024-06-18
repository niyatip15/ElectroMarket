import React, { useState, useEffect } from 'react';
import { Row, Col } from 'react-bootstrap';
import Product from '../components/Product';
import Loader from '../components/Loader';
import Message from '../components/Message'; 
import axios from 'axios';

function HomeScreen() {
    const [products, setProducts] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null); 

    useEffect(() => {
        async function fetchProducts() {
            try {
                const { data } = await axios.get('/api/products/');
                setProducts(data);
                setLoading(false);
            } catch (error) {
                setLoading(false);
                setError('Something went wrong. Please try again later.'); 
                console.error('Error fetching products:', error);
            }
        }

        fetchProducts();
    }, []);

    return (
        <div>
            <h1>Latest Products</h1>
            {loading ? (
                <Loader />
            ) : error ? (
                <Message variant="danger">{error}</Message> 
            ) : (
                <Row>
                    {products.map(product => (
                        <Col key={product._id} sm={12} md={6} lg={4} xl={3}>
                            <Product product={product} />
                        </Col>
                    ))}
                </Row>
            )}
        </div>
    );
}

export default HomeScreen;
