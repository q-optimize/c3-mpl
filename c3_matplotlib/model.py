import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rcParams
from c3.model import Model

rcParams["text.usetex"] = True
rcParams["font.size"] = 12
rcParams["figure.dpi"] = 120


def plot_energy_diamond(model: Model) -> None:
    energies = model.eigenframe.numpy() / np.pi / 2e9
    fig, ax = plt.subplots(1)
    for ii, state in enumerate(model.state_labels):
        manifold = sum(state)
        ax.plot(
            [state[0] - 0.4 - 0.5 * manifold, state[0] + 0.4 - 0.5 * manifold],
            [energies[ii], energies[ii]],
        )
        ax.plot(
            [-10, 10],
            [energies[ii], energies[ii]],
            linewidth=0.5,
            color="black",
            linestyle=":",
            alpha=0.5,
        )
        state_latex = "$|"
        for num in state:
            state_latex += str(num)
        state_latex += "\\rangle$"
        ax.text(
            state[0] - 0.5 * manifold,
            energies[ii] - 0.5,
            state_latex,
            horizontalalignment="center",
            verticalalignment="top",
        )
    ax.set_ylim([energies[0] - 5, energies[-1] * 1.2])
    ax.set_ylabel("Frequency [GHz 2$\\pi$]")
    ax.set_xlim([-0.5 * manifold, 0.5 * manifold])
    ax.get_xaxis().set_visible(False)
    ax.minorticks_on()
