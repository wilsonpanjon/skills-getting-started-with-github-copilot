using QuadraticEquationSolver.Models;

namespace QuadraticEquationSolver.Services;

public class QuadraticEquationService
{
    private const double Tolerance = 1e-10;
    private const int SampleCount = 121;

    public QuadraticSolution Solve(double a, double b, double c)
    {
        if (Math.Abs(a) < Tolerance)
        {
            throw new ArgumentOutOfRangeException(nameof(a), "Coefficient 'a' must be different from zero.");
        }

        var discriminant = (b * b) - (4 * a * c);
        var roots = GetRealRoots(a, b, discriminant);
        var vertexX = -b / (2 * a);
        var vertexY = Evaluate(a, b, c, vertexX);
        var graphPoints = BuildGraphPoints(a, b, c, roots, vertexX);

        return new QuadraticSolution(
            a,
            b,
            c,
            discriminant,
            roots,
            new GraphPoint(vertexX, vertexY),
            graphPoints);
    }

    private static IReadOnlyList<double> GetRealRoots(double a, double b, double discriminant)
    {
        if (discriminant < -Tolerance)
        {
            return [];
        }

        if (Math.Abs(discriminant) <= Tolerance)
        {
            return [(-b) / (2 * a)];
        }

        var squareRoot = Math.Sqrt(discriminant);
        var denominator = 2 * a;

        return
        [
            (-b - squareRoot) / denominator,
            (-b + squareRoot) / denominator
        ];
    }

    private static IReadOnlyList<GraphPoint> BuildGraphPoints(double a, double b, double c, IReadOnlyList<double> roots, double vertexX)
    {
        var maximumReference = new[]
        {
            Math.Abs(vertexX),
            roots.Count > 0 ? roots.Max(Math.Abs) : 0,
            Math.Abs(c)
        }.Max();

        var span = Math.Max(5, maximumReference + 2);
        var startX = vertexX - span;
        var endX = vertexX + span;
        var step = (endX - startX) / (SampleCount - 1);
        var points = new List<GraphPoint>(SampleCount);

        for (var index = 0; index < SampleCount; index++)
        {
            var x = startX + (index * step);
            points.Add(new GraphPoint(x, Evaluate(a, b, c, x)));
        }

        return points;
    }

    private static double Evaluate(double a, double b, double c, double x) => (a * x * x) + (b * x) + c;
}
