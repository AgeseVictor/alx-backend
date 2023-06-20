import kue from 'kue';
const queue = kue.createQueue();

const job = {
  phoneNumber: '25132458723219',
  message: 'This is the code to verify your account',
}
const jobs = queue.create('push_notification_code', job).save((err) => {
  if(!err) console.log(`Notification job created: ${jobs.id}`);
})

jobs.on('complete', function() {
  console.log(' Job completed ');
}).on('failed', function(err, done) {
  console.log('Notification job completed');
})
