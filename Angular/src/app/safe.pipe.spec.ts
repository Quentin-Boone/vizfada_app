import { SafePipe } from './safe.pipe;

describe('Safe', () => {
  it('create an instance', () => {
    const pipe = new SafePipe();
    expect(pipe).toBeTruthy();
  });
});
