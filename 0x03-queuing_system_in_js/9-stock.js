#!/usr/bin/node
/**
 * Stock check
 */
import { promisify } from 'util';
import { createClient } from 'redis';
import express from 'express';

const redisClient = createClient();

redisClient.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

const listProducts = [
  { Id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { Id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { Id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { Id: 4, name: 'Suitcase 1050', price: 550, stock: 5 },
];

const SET_ASYNC = promisify(redisClient.set).bind(redisClient);
const GET_ASYNC = promisify(redisClient.get).bind(redisClient);

async function reserveStockById(itemId, stock) {
  await SET_ASYNC(`item.${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
  const stock = await GET_ASYNC(`item.${itemId}`);
  return stock ? parseInt(stock, 10) : 0;
}

const app = express();

app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const product = listProducts.find((item) => item.Id === itemId);
  if (!product) {
    return res.status(404).json({ status: 'Product not found' });
  }
  const stock = await getCurrentReservedStockById(itemId);
  product.currentQuantity = product.stock - stock;
  res.json(product);
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const product = listProducts.find((item) => item.Id === itemId);
  if (!product) {
    return res.status(404).json({ status: 'Product not found' });
  }
  const stock = await getCurrentReservedStockById(itemId);
  if (stock >= product.stock) {
    return res.status(400).json({ status: 'Not enough stock available', itemId });
  }
  await reserveStockById(itemId, stock + 1);
  res.json({ status: 'Reservation confirmed', itemId });
});

async function clearRedisStock() {
  await redisClient.flushdb();
}

app.listen(1245, async () => {
  await clearRedisStock();
  console.log('API available on localhost via port 1245');
});

