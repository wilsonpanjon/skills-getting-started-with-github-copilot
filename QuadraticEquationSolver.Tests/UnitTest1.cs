using QuadraticEquationSolver.Services;

namespace QuadraticEquationSolver.Tests;

public class QuadraticEquationServiceTests
{
    private readonly QuadraticEquationService _service = new();

    [Fact]
    public void Solve_ReturnsTwoRealRoots_WhenDiscriminantIsPositive()
    {
        var result = _service.Solve(1, -3, 2);

        Assert.Equal(1, result.RealRoots[0], 6);
        Assert.Equal(2, result.RealRoots[1], 6);
        Assert.Equal(1, result.Discriminant, 6);
    }

    [Fact]
    public void Solve_ReturnsSingleRealRoot_WhenDiscriminantIsZero()
    {
        var result = _service.Solve(1, -2, 1);

        var root = Assert.Single(result.RealRoots);
        Assert.Equal(1, root, 6);
        Assert.Equal(0, result.Discriminant, 6);
    }

    [Fact]
    public void Solve_ReturnsNoRealRoots_WhenDiscriminantIsNegative()
    {
        var result = _service.Solve(1, 0, 1);

        Assert.Empty(result.RealRoots);
        Assert.True(result.Discriminant < 0);
    }

    [Fact]
    public void Solve_Throws_WhenAIsZero()
    {
        Assert.Throws<ArgumentOutOfRangeException>(() => _service.Solve(0, 2, 1));
    }
}
