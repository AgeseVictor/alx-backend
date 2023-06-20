function createPushNotificationsJobs(jobs, queue) {
  if (!(jobs instanceof Array)) throw Error('Jobs is not an array'); 

  jobs.forEach((n) => {
    const job = queue.create('push_notification_code_3', n).save((err) => {
      if(!err) console.log(`Notification job created: ${job.id}`);
    });
    job.on('complete', function() {
      console.log(`Notification job ${job.id} completed`);
    }).on('failed', function(err) {
      console.log(`Notification job ${job.id} failed: ${err}`);
    }).on('progress', function(progress) {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });
  });
}
module.exports = createPushNotificationsJobs;
