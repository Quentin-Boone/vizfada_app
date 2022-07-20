import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { FormGroup } from '@angular/forms';

import { IDropdownSettings } from 'ng-multiselect-dropdown';
import { HeatmapInfoService } from '../main/heatmap-info.service';

import { Fields, FieldValues } from './metadata';

@Component({
  selector: 'app-hlfilter',
  template: '<div></div>',
})
export class HLFilterComponent implements OnInit {
  @Input() formGroup: FormGroup;
  @Input() fullFormGroup: FormGroup;

  public FIELDS: Fields;
  
  public fields: string[];
  public formatted_fields: string[];
  public fieldMap: Object = {};
  
  public VALUES: FieldValues;
  
  public values: string[];
  public formatted_values: string[];
  public valuesMap: Object = {};
  
  public selectedValues: string[] = [];
  public selectedFormatted;

  public fieldDropdownSettings: IDropdownSettings = {};
  public valuesDropdownSettings: IDropdownSettings = {};

  constructor(protected heatmapInfoService: HeatmapInfoService) {
    
  }

  ngOnInit(): void {
    this.fieldDropdownSettings = {
      singleSelection: true,
      allowSearchFilter: true,
      closeDropDownOnSelection: true,
      enableCheckAll: false
    };
    this.valuesDropdownSettings = {
      singleSelection: false,
      allowSearchFilter: true,
      enableCheckAll: false
    };
    this.heatmapInfoService.fields.subscribe(fields => {this.FIELDS =fields; this.formatFields();})
    console.log("Fields on init");
    console.log(this.FIELDS);
  }

  // FIELDS

  formatFields(): void {
    console.log("Formatting Fields");
    this.fields = Array.from(Object.keys(this.FIELDS));
    this.formatted_fields = this.fields.map( (field) => {
      return `${this.FIELDS[field]['name']} (${this.FIELDS[field]['count']})`;
    });
    for (let i in this.fields) {
      this.fieldMap[this.formatted_fields[i]] = this.fields[i];
    };
  }

  // VALUES

  getValues(e): void {
    let selected = this.fieldMap[e];
    console.log("Selected ", selected)
    this.formGroup.controls['field'].setValue(selected);
    this.VALUES = this.FIELDS[selected];
    this.formatValues();
  }
  
  formatValues(): void {
    this.values = Object.keys(this.VALUES["values"]);
    console.log("Unformatted values: ", this.values);
    this.formatted_values = this.values.map( (value) => {
      return `${value} (${this.VALUES["values"][value]})`;
    });
    
    for (let i in this.values) {
      this.valuesMap[this.formatted_values[i]] = this.values[i];
    };
    
    console.log("Reformatted values: ", this.valuesMap);
  }

  addSelected(e): void {
    let selected = this.valuesMap[e];
    this.selectedValues.push(selected);
  }

  removeSelected(e): void {
    let i = this.selectedValues.indexOf(e);
    console.log(e, " found at ", i, " in ", this.selectedValues)
    this.selectedValues.splice(i, 1);
    console.log(this.selectedValues)
  }

  onSelectValue(e): void {
    this.addSelected(e);
    console.log("Selected value ", e);
    this.formGroup.controls['values'].setValue(this.selectedValues);
    console.log("selectedFormatted", this.selectedFormatted)
    console.log("Currently selected ", this.formGroup.controls['values']);
  }

  onDeSelectValue(e): void {
    this.removeSelected(e);
    console.log("Deselected value ", e);
    this.formGroup.controls['values'].setValue(this.selectedValues);
    console.log("Currently selected ", this.formGroup.controls['values'])
  }

  onDeselectField(event): void {
    console.log("Called onDeselectField()", this.selectedFormatted)
    this.selectedFormatted = null;
    this.selectedValues = [];
    this.formatted_values = [];
    this.formGroup.controls['values'].setValue([]);
    this.formGroup.controls['field'].setValue('');
    this.heatmapInfoService.update_formGroup(this.fullFormGroup.value);
  }

}
