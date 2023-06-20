import kue from 'kue';
import { expect } from 'chai';
import createPushNotificationsJobs from './8-job';

const queue = kue.createQueue();

const jobs = [
    {
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account'
    }
];

describe('createPushNotificationsJobs', () => {
  before(() => {
    queue.testMode.enter();
  });
  afterEach(() => {
    queue.testMode.clear();
  });
  after(() => {
    queue.testMode.exit();
  });
  it('display an error message', () => {
    expect(() => {
      createPushNotificationsJobs(2, queue);
    }).to.throw('Jobs is not an array');
  });
  it('no error but returns undefined', () => {
    expect(() => {
      const res = createPushNotificationsJobs([], queue);
      expect().to.equal(undefined);
    });
  });
  it('creating jobs', () => {
    queue.createJob('newJob', { Joe: 'seller' }).save();
    queue.createJob('firstJob', { Lui: 'singer' }).save();
    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].type).to.equal('newJob');
    expect(queue.testMode.jobs[0].data).to.eql({ Joe: 'seller' });
    expect(queue.testMode.jobs[1].type).to.equal('firstJob');
    expect(queue.testMode.jobs[1].data).to.eql({ Lui: 'singer' });
  });
});
