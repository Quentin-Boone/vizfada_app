import { Component, Input, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { IDropdownSettings } from 'ng-multiselect-dropdown';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { DataService } from '../../main/data.service';
import { Fields } from '../../utils/metadata';
import { EpistackService } from '../epistack.service';



@Component({
  selector: 'app-menu',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.css']
})
export class MenuComponent implements OnInit {

  public SPECIES : string[];
  public FIELDS : Fields;
  public DEFAULT_FIELDS: Object = {"anchor_type": "Anchor Type",
                                   "cellType": "Cell Type",
                                   "experiment": "Experiment",
                                   "notes": "Notes",
                                   "input_id": "Input DNA",
                                   "bound_id": "Bound ID"};
  
  public formGroup: FormGroup;
  public sortNull() {};
  public fieldMap: Object = {};
  public formatted_fields: string[] = [];
  @Input() side: string;
  
  public fields$: Observable<Fields>;
  public images$: Observable<string[]>;

  public speciesDropdownSettings: IDropdownSettings = {};
  public fieldDropdownSettings: IDropdownSettings = {};

  constructor(private builder: FormBuilder,
              private dataService: DataService,
              private epistackService: EpistackService) { }

  ngOnInit(): void {
    let newForm = this.builder.group({
      species: ["", [Validators.required]],
      anchor_type: "",
      cellType:"",
      input_id:"",
      bound_id:"",
      experiment:"",
      notes:""
    });
    this.formGroup = newForm;
    this.fieldDropdownSettings = {
      singleSelection: true,
      allowSearchFilter: true,
      closeDropDownOnSelection: true,
      enableCheckAll: false
    };
    this.dataService.get_list('species').subscribe(species => {this.SPECIES=species});

    this.formGroup.valueChanges.subscribe(data => {
        this.epistackService.formGroup = this.formGroup;
        this.fields$ = this.getMetaObs();
        this.getImgs();
        this.fields$.subscribe(fields => this.FIELDS = fields);
        console.log("Form value updated")
        console.log(this.formGroup);
      })
  }
  
  patchValue(field, e): void {
    this.formGroup.controls[field].patchValue(e.target.value);
    //this.updateFieldDisplay();
  }
  
  getMetaObs(): Observable<Fields> {
    console.log("getmetaObs called");
    return this.dataService.get_meta('epistack', this.formGroup.value);
  }
  
  getValues(field: string): Observable<Object> {
    this.fields$.pipe(map(fields => fields[field])).subscribe((values) => {
      console.log("getvalues called: ", values)
    });
    return this.fields$.pipe(map(fields => fields[field]));
  }
  
  getImgs(): void {
    this.dataService.get_list('epistack', this.formGroup.value).subscribe( data => {
      this.epistackService.updateImages(this.side, data);
    });
  }
  
  onSubmit(): void {
    console.log("Submitting data");
    console.log(this.formGroup.value);
    this.dataService.get_list('epistack', this.formGroup.value);
  }
  
  isSelected(field, value): boolean {
    return(this.formGroup.get(field).value===value);
  }

}
