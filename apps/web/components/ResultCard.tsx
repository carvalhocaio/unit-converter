type ResultCardProps = {
  summary: string;
  resetHref: string;
};

// Displays the outcome of a conversion, read from the URL search params
// after the Post/Redirect/Get cycle completes.
export function ResultCard({ summary, resetHref }: ResultCardProps) {
  return (
    <div>
      <p>Result of your calculation</p>
      <p className="result-value">{summary}</p>
      <a className="button-link" href={resetHref}>
        Reset
      </a>
    </div>
  );
}
