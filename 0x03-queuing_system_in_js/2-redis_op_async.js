#!/usr/bin/node
/**
 * Connect to redis server via redis client
 */
import redis from 'redis';
import { promisify } from 'util';

const { createClient } = redis;

const client = createClient();

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

const setAsync = promisify(client.set).bind(client);
const getAsync = promisify(client.get).bind(client);

async function setNewSchool(schoolName, value) {
  await setAsync(schoolName, value);
  console.log('Value set successfully');
}

async function displaySchoolValue(schoolName) {
  try {
    const value = await getAsync(schoolName);
    console.log(`Value for key ${schoolName}:`, value);
  } catch (error) {
    console.error('Error retrieving value for key:', error.toString());
  }
}
