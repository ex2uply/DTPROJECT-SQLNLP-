import DotGrid from './DotGrid';

export default function AnimatedBackground() {
  return (
    <div className="fixed inset-0 -z-10 overflow-hidden bg-black">
      <DotGrid
        dotSize={4}
        gap={24}
        baseColor="#4a4a4a"
        activeColor="#ffffff"
        proximity={100}
        shockRadius={100}
        shockStrength={2}
        resistance={750}
        returnDuration={1.5}
      />
    </div>
  );
}
