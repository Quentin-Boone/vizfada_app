export interface FieldValues {
  values: Map<string, number>;
  count: number;
  name: string;
}

export interface Fields {
  field: Map<string, FieldValues>;
}
