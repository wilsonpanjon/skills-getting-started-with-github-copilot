namespace QuadraticEquationSolver.Models;

public sealed record GraphPoint(double X, double Y);

public sealed record QuadraticSolution(
    double A,
    double B,
    double C,
    double Discriminant,
    IReadOnlyList<double> RealRoots,
    GraphPoint Vertex,
    IReadOnlyList<GraphPoint> Points)
{
    public string EquationText => $"{FormatCoefficient(A, true)}x² {FormatCoefficient(B)}x {FormatCoefficient(C)} = 0";

    private static string FormatCoefficient(double value, bool isFirst = false)
    {
        var absoluteValue = Math.Abs(value).ToString("0.###");

        if (isFirst)
        {
            return value < 0 ? $"-{absoluteValue}" : absoluteValue;
        }

        return value < 0 ? $"- {absoluteValue}" : $"+ {absoluteValue}";
    }
}
