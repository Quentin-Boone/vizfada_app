import { Component, Input, OnInit } from '@angular/core';
import { FormGroup } from '@angular/forms';
import { HLFilterComponent } from '../../../utils/hlfilter';
import { HeatmapInfoService } from '../../heatmap-info.service';

@Component({
  selector: 'app-filter',
  templateUrl: './filter.component.html',
  styleUrls: ['./filter.component.css']
})
export class FilterComponent extends HLFilterComponent implements OnInit {

  constructor(heatmapInfoService: HeatmapInfoService) {
    super(heatmapInfoService);
  }

  ngOnInit(): void {
    super.ngOnInit()
  }




/*
    this.fieldDropdownSettings = {
      singleSelection: true,
      allowSearchFilter: true,
      closeDropDownOnSelection: true,
      enableCheckAll: false
    };
    this.valuesDropdownSettings = {
      singleSelection: false,
      allowSearchFilter: true,
    };
    
    this.fields = Array.from(Object.keys(this.FIELDS));
    this.formatted_fields = this.fields.map( (field) => {
      return `${this.FIELDS[field]['name']} (${this.FIELDS[field]['count']})`;
    });
    for (let i in this.fields) {
      this.fieldMap[this.formatted_fields[i]] = this.fields[i];
    };
    
    console.log(this.fields);
  }

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
    let selected = this.valuesMap[e];
    let i = this.selectedValues.indexOf(e);
    console.log(e, " found at ", i, " in ", this.selectedValues)
    this.selectedValues.splice(i, 1);
    console.log(this.selectedValues)
  }

  onSelectValue(e): void {
    let selected = this.addSelected(e);
    console.log("Selected value ", e);
    this.formGroup.controls['values'].setValue(this.selectedValues);
    console.log("Currently selected ", this.formGroup.controls['values'])
  }

  onDeSelectValue(e): void {
    let selected = this.removeSelected(e);
    console.log("Deselected value ", e);
    this.formGroup.controls['values'].setValue(this.selectedValues);
    console.log("Currently selected ", this.formGroup.controls['values'])
  }
  
  onSelectAllValues(e): void {
    for (let value of e) {
      this.onSelectValue(value);
    }
  }
*/
}
