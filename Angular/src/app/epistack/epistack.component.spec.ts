import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EpistackComponent } from './epistack.component';

describe('EpistackComponent', () => {
  let component: EpistackComponent;
  let fixture: ComponentFixture<EpistackComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ EpistackComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(EpistackComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
