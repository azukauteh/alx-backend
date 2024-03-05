#!/usr/bin/node
/**
 * Create a job
 */
import { createQueue } from 'kue';

const queue = createQueue();
const jobData = { phoneNumber: '+27653454230', message: ' verify your identification' };

const job = queue.create('push_notification_code', jobData);

job.on('enqueue', () => {
  console.log(`Notification job created: ${job.id}`);
});

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
});

job.save((err) => {
  if (err) {
    console.error('Error creating job:', err);
  }
});
