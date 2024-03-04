#!/usr/bin/node
/**
 * Connect to redis server via redis client
 */
import redis from 'redis';

const { createClient } = redis;

const client = createClient();

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, reply) => {
    if (err) {
      console.error('Error retrieving value for key:', err.toString());
      return;
    }
    console.log(`Value for key ${schoolName}:`, reply);
  });
}

