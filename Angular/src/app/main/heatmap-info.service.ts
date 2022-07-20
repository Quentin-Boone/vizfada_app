import { Injectable } from '@angular/core';
import { FormGroup } from '@angular/forms';
import { ReplaySubject, BehaviorSubject, Observable} from 'rxjs';
import { Fields } from '../utils/metadata';
import { DataService } from './data.service';


@Injectable({
  providedIn: 'root'
})
export class HeatmapInfoService {

  public pxcolor = new ReplaySubject;
  public imgLoaded = new BehaviorSubject(false);
  public plotlyBool = new BehaviorSubject(false);
  public fields = new ReplaySubject<Fields>();
  public formGroup = new ReplaySubject<FormGroup>();

  constructor(private dataService: DataService) {
    this.formGroup.subscribe(formGroup => {this.get_metadata(formGroup)})
  }

  pixel_color(color: string): void {
    this.pxcolor.next(color);
  }

  img_loaded(bool: boolean): void {
    this.imgLoaded.next(bool);
  }
  
  set_plotlyBool(bool: boolean): void {
    this.plotlyBool.next(bool);
  }

  update_formGroup(formGroup: FormGroup): void {
    this.formGroup.next(formGroup)
  }

  private get_metadata(formGroup: FormGroup): void {
    this.dataService.get_meta('fields', formGroup)
                    .subscribe(meta => {this.fields.next(meta)});
  }

}
