//! Shared browser-game contract and solver/validator traits.

/// A game action submitted by a player or bot.
pub trait Action: Clone + Send + Sync + 'static {}

/// A deterministic game state.
pub trait GameState: Clone + Send + Sync + 'static {}

/// A game rules implementation used by the server and bot training.
pub trait Game: Send + Sync + 'static {
    type State: GameState;
    type Action: Action;

    fn initial(&self) -> Self::State;
    fn apply(&self, state: &Self::State, action: &Self::Action) -> Option<Self::State>;
    fn legal_actions(&self, state: &Self::State) -> Vec<Self::Action>;
}

/// Reference value used by the CLI and tests.
pub fn answer() -> i32 {
    42
}
