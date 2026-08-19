type UnitOption = {
  value: string;
  label: string;
};

type ConversionFormProps = {
  action: (formData: FormData) => void;
  fieldLabel: string;
  units: UnitOption[];
};

// Pure presentational Server Component. The `action` prop is a Server
// Action reference — the browser posts the form directly to the server,
// no client JS or fetch() involved.
export function ConversionForm({ action, fieldLabel, units }: ConversionFormProps) {
  return (
    <form action={action}>
      <div className="field">
        <label htmlFor="value">{fieldLabel}</label>
        <input id="value" name="value" type="number" step="any" required />
      </div>

      <div className="field">
        <label htmlFor="from">Unit to convert from</label>
        <select id="from" name="from" defaultValue={units[0]?.value} required>
          {units.map((unit) => (
            <option key={unit.value} value={unit.value}>
              {unit.label}
            </option>
          ))}
        </select>
      </div>

      <div className="field">
        <label htmlFor="to">Unit to convert to</label>
        <select id="to" name="to" defaultValue={units[1]?.value ?? units[0]?.value} required>
          {units.map((unit) => (
            <option key={unit.value} value={unit.value}>
              {unit.label}
            </option>
          ))}
        </select>
      </div>

      <button type="submit">Convert</button>
    </form>
  );
}
