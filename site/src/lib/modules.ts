/**
 * Short glosses for the project axes SchemaTracker walks. Only modules whose role is
 * unambiguous from the binary they come from are listed; everything else falls back
 * to the binary names recorded in the artifact.
 */
const GLOSS: Record<string, string> = {
	client: 'Client-side entity representations. Names are usually the server class prefixed with C_, and offsets differ from the server twin.',
	server: 'Server-side game logic entities: pawns, controllers, weapons, game rules and the services hanging off them.',
	entity2: 'The entity system itself: instance identity, entity handles, components and the base classes both client and server build on.',
	engine2: 'Engine-level types shared by every subsystem, including the entity system host and networked scene state.',
	networksystem: 'Networking primitives: channels, message routing and the transport-facing types.',
	schemasystem: 'The reflection system that describes every other type here.',
	resourcesystem: 'Resource handles, references and the manifest types that back asset loading.',
	materialsystem2: 'Material and shader parameter types.',
	particles: 'Particle system operators, initializers, renderers and their parameter blocks.',
	particleslib: 'Shared particle definitions used by both the runtime and the tools.',
	animgraphlib: 'Animation graph nodes, tags, parameters and their runtime state.',
	animationsystem: 'Skeletons, sequences, pose parameters and the animation runtime.',
	animlib: 'Lower-level animation containers shared by the animation runtime and the tools.',
	pulse_runtime_lib: 'Pulse graph runtime: cells, instructions and the values that flow between them.',
	pulse_system: 'Pulse graph definitions and the descriptor types the runtime instantiates.',
	physicslib: 'Physics shapes, aggregates and collision attributes.',
	vphysics2: 'The physics engine types behind bodies, joints and soft bodies.',
	soundsystem: 'Sound events, mixers and the operator stacks that drive them.',
	scenesystem: 'Scene graph and render-view types.',
	worldrenderer: 'World geometry, node trees and the built world layers.',
	modellib: 'Model, mesh and material group data as it exists at runtime.',
	hammer: 'Level editor types. Tool-side only, with no runtime counterpart.',
	smartprops: 'Smart prop definitions: element rules, selection criteria and variables.',
	tier2: 'Shared low-level utility types.',
	mathlib_extended: 'Math primitives beyond the built-in vector and matrix types.',
};

export function moduleGloss(module: string): string | undefined {
	return GLOSS[module];
}
