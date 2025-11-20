import DotGrid from './DotGrid';

export default function AnimatedBackground() {
  return (
    <div className="fixed inset-0 -z-10 overflow-hidden bg-black">
      <DotGrid
        dotSize={4}
        gap={24}
        baseColor="#4a4a4a"
        activeColor="#ffffff"
        proximity={60}
        shockRadius={60}
        shockStrength={1}
        resistance={2000}
        returnDuration={3.0}
      />
    </div>
  );
}
