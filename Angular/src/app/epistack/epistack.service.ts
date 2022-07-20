import { Injectable } from '@angular/core';
import { FormGroup } from '@angular/forms';
import { Subject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class EpistackService {
  
  public formGroup: FormGroup;
  public leftImages$ = new Subject<string[]>();
  public rightImages$ = new Subject<string[]>();

  constructor() { }
  
  updateImages(side:string, imgs: string[]): void {
    console.log(side, "panel updating");
    if (side === "left") {
      this.leftImages$.next(imgs);
      console.log("Left images updated : ", imgs.length)
    } else if (side === "right") {
      this.rightImages$.next(imgs);
      console.log("Right images updated : ", imgs.length)
    }
  }
  
}
